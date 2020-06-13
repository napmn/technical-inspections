<template>
  <b-row id="stations" class="border">
    <b-col cols="3">
      <h4>Stanice</h4>
      <div>Počet stanic:</div>
      <div>Zkontrolovaných vozidel:</div>
      <div>Úspěšnost:</div>
      <div>Podporované typy vozidel:</div>
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
  props: ['selectedRegion'],
  data() {
    return {
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
      this.fillLineData(newVal);
      this.fillBarData(newVal);
    }
  },
  mounted() {
    this.fillLineData(null);
    this.fillBarData(null);
  },
  methods: {
    fillBarData(region) {
      let data1, data2;
      if (region === null) {
        data1 = [18, 28, 12, 10, 15, 13, 14, 8, 8, 20, 11, 23];
        data2 = [10, 13, 8, 16, 12, 7, 11, 12, 10, 6, 16, 17];
      }
      else {
        data1 = [8, 11, 5, 10, 6, 6, 9, 5, 5, 6, 8, 12];
        data2 = [10, 13, 8, 10, 12, 7, 8, 12, 10, 4, 16, 15];
      }
      this.bardatacollection = {
        labels: ['Rutinná', 'TSK', 'ADR', 'BATCV', 'Před registrací'],
        datasets: [
          {
            label: 'Opakované prohlídky',
            backgroundColor: '#36a2eb',
            // borderColor
            data: data1
          },
          {
            label: 'Prvotné prohlídky',
            backgroundColor: '#f87979',
            data: data2
          }
        ]
      }
    },
    fillLineData(region) {
      let data1, data2;
      if (region === null) {
        data1 = [10, 13, 8, 16, 12, 7, 11, 12, 10, 12, 16, 17];
        data2 = [18, 28, 12, 22, 15, 13, 14, 20, 11, 14, 18, 23];
      }
      else {
        data1 = [8, 11, 5, 10, 6, 6, 9, 5, 5, 6, 8, 12];
        data2 = [10, 13, 8, 10, 12, 7, 13, 12, 10, 10, 16, 15];
      }
      this.datacollection = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            fill: 'start',
            label: 'Úspešné prohlídky',
            backgroundColor: '#36a2eb',
            // borderColor
            data: data1
          },
          {
            fill: 'start',
            label: 'Všechny prohlídky',
            backgroundColor: '#f87979',
            data: data2
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

</style>
