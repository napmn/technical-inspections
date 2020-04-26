<template>
  <div>
    <b-button size="sm" @click="changeAttribute">
    Toggle
    </b-button>
    <div id="cz-map">
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import * as topojson from 'topojson-client';
import d3Tip from 'd3-tip';


export default {
  name: 'CzMap',
  props: ['svgWidth', 'svgHeight'],
  data() {
    return {
      topoData: {},
      centered: null,
      activeAttribute: 'stationsNumber',
      stats: [
        {
          name: 'Středočeský',
          stationsNumber: 10,
          passRate: 0.9
        },
        {
          name: 'Ústecký',
          stationsNumber: 20,
          passRate: 0.92
        },
        {
          name: 'Jihočeský',
          stationsNumber: 25,
          passRate: 0.88
        },
        {
          name: 'Jihomoravský',
          stationsNumber: 40,
          passRate: 0.85
        },
        {
          name: 'Karlovarský',
          stationsNumber: 15,
          passRate: 0.9
        },
        {
          name: 'Královéhradecký',
          stationsNumber: 44,
          passRate: 0.89
        },
        {
          name: 'Liberecký',
          stationsNumber: 26,
          passRate: 0.83
        },
        {
          name: 'Kraj Vysočina',
          stationsNumber: 33,
          passRate: 0.91
        },
        {
          name: 'Moravskoslezský',
          stationsNumber: 38,
          passRate: 0.87
        },
        {
          name: 'Olomoucký',
          stationsNumber: 30,
          passRate: 0.92
        },
        {
          name: 'Pardubický',
          stationsNumber: 18,
          passRate: 0.84
        },
        {
          name: 'Plzeňský',
          stationsNumber: 31,
          passRate: 0.98
        },
        {
          name: 'Praha',
          stationsNumber: 6,
          passRate: 0.90
        },
        {
          name: 'Zlínský',
          stationsNumber: 18,
          passRate: 0.87
        }
      ] // TODO: connect to API
    }
  },
  created() {
    this.colors = {
      stationsNumber: d3.scaleSequential(d3.interpolateBlues),
      passRate: d3.scaleSequential(d3.interpolateGreens)
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
    activeAttribute() {
      this.updateMap();
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
          return '<span>Kraj: ' + d.properties.NAME_1 + '</span><br>'
            + '<span>Počet stanic: ' + d.stationsNumber + '</span><br>'
            + '<span>Míra úspěšnosti: ' + d.passRate + '</span>'
        });
      this.detailedTip = d3Tip()
        .attr('id', 'd3-tip-detailed')
        .attr('class', 'd3-tip')
        .offset([10, 0])
        .html((d) => {
          return '<span>Skuska detailu</span><br>'
          + '<span>Kraj: ' + d.properties.NAME_1 + '</span'
        });
    },
    createSvg() {
      this.svg = d3.select('#cz-map')
        .append('svg')
        .attr('width', this.svgWidth)
        .attr('height', this.svgHeight);
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
    updateColorAndScaleByActiveAttribute() {
      let maxVal = d3.max(this.stats.map(d => d[this.activeAttribute]));
      let minVal = d3.min(this.stats.map(d => d[this.activeAttribute]));
      this.colors[this.activeAttribute].domain([minVal, maxVal]);
      this.scale.domain([minVal, maxVal]).nice();
      this.legend.select('#legend-zero').attr("stop-color", this.colors[this.activeAttribute](maxVal));
      this.legend.select('#legend-hundred').attr("stop-color", this.colors[this.activeAttribute](minVal));
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
          .transition()
          .duration(800)
          .style('fill', d => this.colors[this.activeAttribute](d[this.activeAttribute]))
          .style('opacity', 1)
    },
    updateMap() {
      console.log('update map');
      this.svg.selectAll('.axis').remove();

      this.stats.map(d => {
        let region = this.topoRegions.features.find(r => r.properties.NAME_1 == d.name);
        if (region) {
          region.stationsNumber = d.stationsNumber;
          region.passRate = d.passRate;
        }
      });

      this.updateColorAndScaleByActiveAttribute();
      this.updateAxis();
      this.drawRegions();
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
        console.log('Focused on ' + d.properties.NAME_1);
      } else {
        x = this.svgWidth / 2;
        y = this.svgHeight / 2;
        k = 1;
        this.centered = null;
        console.log('Focused on all')
      }

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
    changeAttribute() { // TODO: this is only dummy method
      if (this.activeAttribute == 'stationsNumber') {
        this.activeAttribute = 'passRate';
      }
      else {
        this.activeAttribute = 'stationsNumber';
      }
      console.log('Active attribute is now ' + this.activeAttribute);
    }
  }
}
</script>
