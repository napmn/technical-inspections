<template>
  <b-row>
    <b-col cols="11" id="cz-map"></b-col>
    <b-col class="text-center">
      <div class="pb-5">
        <h4>Výběr aktivní dimenze</h4>
        <div><b-button block size="sm" @click="setActiveDimension('number_of_stations')"
          :class="[activeDimension=='number_of_stations'?'active':'not-active', 'mt-2']">Počet stanic</b-button></div>
        <div><b-button block size="sm" @click="setActiveDimension('number_of_inspections')"
          :class="[activeDimension=='number_of_inspections'?'active':'not-active', 'mt-2']">Počet kontrol</b-button></div>
        <div><b-button block size="sm" @click="setActiveDimension('pass_rate')"
          :class="[activeDimension=='pass_rate'?'active':'not-active', 'mt-2']">Míra úspěšnosti</b-button></div>
      </div>
      <div class="border rounded mt-5 p-2 legend">
        <h4 class="">Legenda</h4>
        <div class="text-left">
          Zabarvení krajů odpovídá hodnotě kterou kraj nabývá pro vybranou dimenzi.
        </div>
        <div class="text-left pt-2">
          Kroužky, které se objeví po přiblížení mapy označují stanice.
          Barva kroužku vyjadřuje míru úspěšnosti v dané stanici.
        </div>
      </div>
    </b-col>
  </b-row>
</template>

<script>
import * as d3 from 'd3';
import * as topojson from 'topojson-client';
import d3Tip from 'd3-tip';


export default {
  name: 'CzMap',
  props: ['svgWidth', 'svgHeight', 'selectedRegion', 'stations', 'precalculatedStats'],
  data() {
    return {
      topoData: {},
      centered: null,
      localPrecalculatedStats: null,
      activeDimension: 'number_of_stations',
      strokeColors: {
        number_of_stations: 'aqua',
        number_of_inspections: 'darkorange',
        pass_rate: 'limegreen'
      }
    }
  },
  computed: {
    localSelectedRegion: {
      get: function() {
        return this.selectedRegion;
      },
      set: function(value) {
        this.$emit('update:selectedRegion', value)
      }
    }
  },
  created() {
    this.colors = {
      number_of_stations: d3.scaleSequential(d3.interpolateBlues),
      number_of_inspections: d3.scaleSequential(d3.interpolateOranges),
      pass_rate: d3.scaleSequential(d3.interpolateGreens)
    }
    this.scale = d3.scaleLinear().range([0, this.svgWidth / 2]);
  },
  mounted() {
    this.createTooltips();
    this.createSvg();
    this.loadData().then(_ => {
      this.drawMap();
      this.updateMap();
    });
    // draw legend rect
    this.legend = this.svg.append("defs")
      .append("svg:linearGradient")
      .attr("id", "gradient")
      .attr("x1", "100%")
      .attr("y1", "100%")
      .attr("x2", "0%")
      .attr("y2", "100%")
      .attr("spreadMethod", "pad");

    this.legend.append("stop").attr('id', 'legend-zero').attr("offset", "0%");
    this.legend.append("stop").attr('id', 'legend-hundred').attr("offset", "100%");

    this.svg.append("rect")
        .attr("width", this.svgWidth / 2)
        .attr("height", 10)
        .style("fill", "url(#gradient)")
        .attr("transform", `translate(${this.svgWidth/4},${this.svgHeight-35})`);
  },
  watch: {
    activeDimension() {
      this.updateMap();
    },
    precalculatedStats(newVal, oldVal) {
      this.localPrecalculatedStats = newVal.filter(d => d.region !== null);
      this.localPrecalculatedStats.forEach(d => {
        let total = d.eligible + d.partially_eligible + d.ineligible;
        if (total == 0) {
          d.pass_rate = 0.5;
        } else {
          d.pass_rate = (d.eligible + d.partially_eligible) / (total);
        }
      })
      this.updateMap();
    },
    localSelectedRegion(newVal, oldVal) {
      if (this.centered === newVal || (this.centered !== null && this.centered.properties.NAME_1 === newVal)) {
        // region was not changed so dont change focus
        return;
      }
      if (newVal === null) {
        // remove focus from region
        this.clicked(null);
      } else {
        // find svg path for selected region and focus on it
        let selectedPath = this.svgG.selectAll('path.region').filter(function(d, i) {
          return d3.select(this).data()[0].properties.NAME_1 == newVal;
        })
        this.clicked(selectedPath.data()[0])
      }
    },
    stations(newVal, oldVal) {
      if (newVal) {
        this.updateMap();
      }
    }
  },
  methods: {
    async loadData() {
      let data = await d3.json('../../static/cz_map.json');
      this.topoData = data;
    },
    createTooltips() {
      this.generalTip = d3Tip()
        .attr('id', 'd3-tip-general')
        .attr('class', 'd3-tip')
        .offset([10, 0])
        .html((d) => {
          return '<span class="d3-tip-bold">Kraj: ' + d.properties.NAME_1 + '</span><br>'
            + '<span>Počet stanic: ' + d.number_of_stations + '</span><br>'
            + '<span>Počet kontrol: ' + d.number_of_inspections + '</span><br>'
            + `<span">Míra úspěšnosti: ${(d.pass_rate*100).toFixed(3)}%</span><br>`
        });
      this.detailedTip = d3Tip()
        .attr('id', 'd3-tip-detailed')
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html((d) => {
          return '<span class="d3-tip-bold">Detail stanice</span><br>'
          + `<span>Provozovatel: ${d.operator}</span><br>`
          + `<span>Adresa: ${d.address}, ${d.city}</span><br>`
          + `<span>Oprávnění: ${d.authorization}</span><br><br>`
          + `<span class="d3-tip-bold">Kontakt</span><br>`
          + `<span>Tel. č.: ${d.tel_number}</span><br>`
          + `<span>Email: ${d.email}</span><br><br>`
          + `<span class="d3-tip-bold">Statistiky</span><br>`
          + `<span>Počet kontrol: ${d.number_of_inspections}</span><br>`
          + `<span>Míra úspěšnosti: ${(d.pass_rate*100).toFixed(3)}%</span><br>`
        });
    },
    createSvg() {
      this.svg = d3.select('#cz-map')
        .append('svg')
        .attr("preserveAspectRatio", "xMinYMin meet")
        .attr("viewBox", `0 0 ${this.svgWidth} ${this.svgHeight}`)
      this.svgG = this.svg.append('g');
      this.svgG.call(this.generalTip);
      this.svgG.call(this.detailedTip);
    },
    drawMap() {
      console.log('draw map')
      let projection = d3.geoNaturalEarth1();
      this.pathGenerator = d3.geoPath().projection(projection);

      this.topoRegions = topojson.feature(this.topoData, this.topoData.objects.CZE_adm1);
      this.pathGenerator.projection().fitSize([this.svgWidth, this.svgHeight], this.topoRegions);
    },
    updateColorAndScaleByactiveDimension() {
      let maxVal = d3.max(this.localPrecalculatedStats.map(d => d[this.activeDimension]));
      let minVal = d3.min(this.localPrecalculatedStats.map(d => d[this.activeDimension]));
      this.colors[this.activeDimension].domain([minVal, maxVal]);
      this.scale.domain([minVal, maxVal]).nice();
      this.legend.select('#legend-zero').attr("stop-color", this.colors[this.activeDimension](maxVal));
      this.legend.select('#legend-hundred').attr("stop-color", this.colors[this.activeDimension](minVal));
    },
    drawRegions() {
      let regionPaths = this.svgG.selectAll('path.region')
        .data(this.topoRegions.features)

      regionPaths.enter()
        .append('path')
        .attr('class', 'region')
        .classed('unzoomed', true)
        .attr('d', this.pathGenerator)
        .on('click', this.clicked)
        .on('mouseover', this.generalTip.show)
        .on('mouseout', this.generalTip.hide)
        .merge(regionPaths)
          .style('opacity', 0.5)
          .style('stroke', this.strokeColors[this.activeDimension])
          .transition()
          .duration(800)
          .style('fill', d => this.colors[this.activeDimension](d[this.activeDimension]))
          .style('opacity', 1)
    },
    updateMap() {
      console.log('update map');
      if (this.localPrecalculatedStats && this.stations) {
        console.log('update map inside');
        this.svg.selectAll('.axis').remove();

        this.localPrecalculatedStats.map(d => {
          let region = this.topoRegions.features.find(r => r.properties.NAME_1 == d.region);
          if (region) {
            region.number_of_stations = d.number_of_stations;
            region.number_of_inspections = d.number_of_inspections;
            region.pass_rate = d.pass_rate;
          }
        });

        this.updateColorAndScaleByactiveDimension();
        this.updateAxis();
        this.drawRegions();

        this.colors.pass_rate.domain([0.95, 1]);

        let stationGlyphs = this.svgG.selectAll('circle.station')
          .data(this.stations);
        stationGlyphs.enter()
          .append('circle')
          .attr('class', 'station')
          .attr('cx', d => d.map_x)
          .attr('cy', d => d.map_y)
          .attr('r', 2)
          .style('opacity', 0)
          .style('fill', d => this.colors.pass_rate(d.pass_rate));
      }
    },
    clicked(d) {
      var x, y, k;

      if (d && this.centered !== d) {
        var centroid = this.pathGenerator.centroid(d);
        x = centroid[0];
        y = centroid[1];
        k = 2.5;
        this.centered = d;
        this.generalTip.hide();
        this.localSelectedRegion = d.properties.NAME_1;
        console.log('Focused on ' + d.properties.NAME_1);
      } else {
        x = this.svgWidth / 2;
        y = this.svgHeight / 2;
        k = 1;
        this.centered = null;
        this.localSelectedRegion = null;
        this.detailedTip.hide();
        console.log('Focused on all')
      }

      this.svgG.selectAll('circle.station')
          .on('mouseover', this.centered ? this.detailedTip.show : undefined)
          .on('mouseout', this.centered ? this.detailedTip.hide : undefined)
          .transition()
          .duration(750)
          .style('opacity', this.centered ? 1 : 0)

      this.svgG.selectAll('path')
          .classed('inactive', this.centered && ((p) => { return p != this.centered }))
          .classed('unzoomed', this.centered ? false : true)
          .on('mouseover', this.centered ? undefined : this.generalTip.show)
          .on('mouseout', this.centered ? undefined : this.generalTip.hide)

      this.svgG.transition()
          .duration(750)
          .attr('transform', 'translate(' + this.svgWidth / 2 + ',' + this.svgHeight / 2 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')')
          .style('stroke-width', 1.5 / k + 'px');

    },
    updateAxis() {
      let axis = d3.axisBottom().scale(this.scale);
      this.svg.append("g")
        .attr("class", "axis")
        .attr("transform", `translate(${this.svgWidth/4},${this.svgHeight - 20})`)
        .transition()
        .duration(800)
        .call(axis);
    },
    setActiveDimension(dimension) {
      this.activeDimension  = dimension
    }
  }
}
</script>

<style scoped>
#cz-map {
  max-width: 900px;
  max-height: 500px;
}
.active {

}
.not-active {
  opacity: 0.4
}
</style>
