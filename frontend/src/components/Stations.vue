<template>
  <b-row id="stations" class="pb-2">
    <b-col cols="3" class="pt-2">
      <h3>Stanice</h3>
      <h5 class="pt-3">Počet stanic: {{ selectedStations.numberOfStations }}</h5>
      <h5>Počet vykonaných kontrol: {{ selectedStations.numberOfInspections }}</h5>
      <h5>Úspěšnost: {{ selectedStations.passRate }}%</h5>
    </b-col>
    <b-col cols="5">
      <LineChart :chart-data="datacollection" :options="lineChartOptions" class="justify-content-center"/>
    </b-col>
    <b-col cols="4">
      <BarChart :chart-data="bardatacollection" :options="barChartOptions"/>
    </b-col>
  </b-row>
</template>

<script>
import LineChart from './LineChart'
import BarChart from './BarChart'


export default {
  name: 'Stations',
  components: {
    LineChart,
    BarChart
  },
  props: ['selectedRegion', 'selectedVehicle', 'stations', 'precalculatedStats'],
  data() {
    return {
      selectedStations: {
        numberOfStations: 0,
        numberOfInspections: 0,
        passRate: 0
      },
      datacollection: {},
      bardatacollection: {},
      lineChartOptions: {
        maintainAspectRatio: false,
        tooltips: {
          mode: 'index',
          intersect: false,
        }
      },
      barChartOptions: {
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }],
          xAxes: [{
            stacked: true,
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    }
  },
  watch: {
    selectedRegion(newVal, oldVal) {
      if (this.selectedVehicle || this.precalculatedStats === null) { // use stations
        // TODO
      } else {
        this.usePrecalculatedStats(this.precalculatedStats.find(obj => obj.region == this.selectedRegion))
      }
      this.fillLineData(newVal);
      this.fillBarData(newVal);
    },
    precalculatedStats(newVal, oldVal) {
      if (this.selectedVehicle){ // TODO: precalculated stats should be used only without selected vehicle
        this.usePrecalculatedStats(newVal.find(obj => obj.region == this.selectedRegion));
      } else {
        this.usePrecalculatedStats(newVal.find(obj => obj.region == this.selectedRegion));
      }
      this.fillLineData(this.selectedRegion);
      this.fillBarData(this.selectedRegion);
    },
    stations(newVal, oldVal) {
      if (this.selectedVehicle) {
        // TODO
      }
    }
  },
  mounted() {
    // this.fillLineData(null);
    // this.fillBarData(null);
  },
  methods: {
    filterStatsForBarData(inspectionStats, repeated) {
      return inspectionStats.filter(obj => obj.repeated == repeated)
        .sort((a, b) => (a.inspection_type > b.inspection_type) ? 1 : ((b.inspection_type > a.inspection_type) ? -1 : 0))
        .map(obj => obj.number_of_inspections);
    },
    prepareDataForLineChart(data, ) {

    },
    usePrecalculatedStats(precalculatedItem) {
      this.selectedStations.numberOfStations = precalculatedItem.number_of_stations;
      this.selectedStations.numberOfInspections = precalculatedItem.number_of_inspections;
      let passed = precalculatedItem.eligible + precalculatedItem.partially_eligible;
      this.selectedStations.passRate = (passed / (passed + precalculatedItem.ineligible) * 100).toFixed(3);
    },
    fillBarData(region) {
      let stats = this.precalculatedStats.find(obj => obj.region == region);
      let labels = [...new Set(stats.inspectiontypestatistic_set.map(obj => obj.inspection_type))].sort();
      let repeated = this.filterStatsForBarData(stats.inspectiontypestatistic_set, true);
      let notRepeated = this.filterStatsForBarData(stats.inspectiontypestatistic_set, false);

      this.bardatacollection = {
        labels: labels,
        datasets: [
          {
            label: 'Opakované prohlídky',
            backgroundColor: '#23347e',
            // borderColor
            data: repeated
          },
          {
            label: 'Prvotné prohlídky',
            backgroundColor: '#facf6a',
            data: notRepeated
          }
        ]
      }
    },
    fillLineData(region) {
      let stats = this.precalculatedStats.find(obj => obj.region == region);
      let allInspections = stats.inspectionsinmonth_set.sort((a, b) => a.month - b.month)
        .map(d => d.passed + d.not_passed);
      let successfull = stats.inspectionsinmonth_set.sort((a, b) => a.month - b.month)
        .map(d => d.passed);

      this.datacollection = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            fill: false,
            label: 'Úspešné prohlídky',
            backgroundColor: '#facf6a',
            borderColor: '#facf6a',
            data: successfull
          },
          {
            fill: false,
            label: 'Všechny prohlídky',
            backgroundColor: '#23347e',
            borderColor: '#23347e',
            data: allInspections
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }
}
</script>
<style scoped>
#stations {
  margin-top: 10px;
}
</style>
