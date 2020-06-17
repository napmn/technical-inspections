<template>
  <div class="vehicles">
    <b-row><h3>Vozidlo</h3></b-row>
    <div v-if="localSelectedVehicle">
      <b-row>
        <b-col>Značka a model: {{ localSelectedVehicle }}</b-col>
      </b-row>
      <b-row>
        <b-col >Typ vozidla: {{ vehicleStats.vehicleType }}</b-col>
        <b-col >Průměrný počet km: {{ vehicleStats.averageKm }}</b-col>
      </b-row>
    </div>
    <div v-else>
      <b-row>
        <b-col>Značka a model: Všechy vozidla</b-col>
      </b-row>
      <b-row>
        <b-col>Typ vozidla: ---</b-col>
        <b-col>Průměrný počet km: {{ vehicleStats.averageKm }}</b-col>
      </b-row>
    </div>
    <b-row class="mt-3 border-top mr-3 pt-3">
      <b-col>
      <div class="w-100 text-center"><h5>Rank vozidla</h5></div>
      <div class="w-100 text-center" v-if="selectedVehicle">
        <div class="rank-5">{{ vehicleStats.rank - 2 }} - TMP</div>
        <div class="rank-2">{{ vehicleStats.rank - 1 }} - TMP</div>
        <div class="rank-main">{{ vehicleStats.rank }} - {{ selectedVehicle }}</div>
        <div class="rank-2">{{ vehicleStats.rank + 1 }} - TMP</div>
        <div class="rank-5">{{ vehicleStats.rank + 2 }} - TMP</div>
      </div>
      <div class="w-100 text-center" v-else>
        <div class="rank-main text-center">1 - MAZDA SD-E</div>
        <div class="rank-2">2 - MERCEDES GLE 350</div>
        <div class="rank-3">3 - ŠKODA YETI</div>
        <div class="rank-4">4 - BMW M550</div>
        <div class="rank-5">5 - SEAT ALTEA FREETRACK</div>
      </div>
      </b-col>
    </b-row>
      <FaultLineChart class="mt-3" :chart-data="faultChartKmDataCollection" :options="faultKmOptions"/>
      <FaultLineChart class="border-bottom" :chart-data="faultChartAgeDataCollection" :options="faultAgeOptions"/>
  </div>
</template>

<script>
import EmissionBarChart from './EmissionBarChart'
import FaultLineChart from './FaultLineChart'


export default {
  name: 'Vehicles',
  components: {
    EmissionBarChart,
    FaultLineChart
  },
  data() {
    return {
      faultChartKmDataCollection: {},
      faultChartAgeDataCollection: {},
      faultKmOptions: {
        maintainAspectRatio: false,
        tooltips: {
          mode: 'index',
          intersect: false,
        },
        elements: {
          point:{
            radius: 0
          }
        },
        scales: {
          yAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Počet závad'
            }
          }],
          xAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Počet najetých kilometrů'
            }
          }]
        }
      },
      faultAgeOptions: {
        maintainAspectRatio: false,
        tooltips: {
          mode: 'index',
          intersect: false,
        },
        elements: {
          point:{
            radius: 0
          }
        },
        legend: {
          display: false
        },
        scales: {
          yAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Počet závad'
            }
          }],
          xAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Věk vozidla'
            }
          }]
        }
      },
      vehicleStats: {
        averageKm: 158357,
        vehicleType: '---',
        rank: 0
      }
    }
  },
  mounted() {
    this.fillLineAgeData(null);
    this.fillLineKmData(null);
  },
  props: ['selectedVehicle'],
  computed: {
    localSelectedVehicle: {
      get: function() {
        return this.selectedVehicle;
      },
      set: function(value) {
        this.$emit('update:selectedVehicle', value)
      }
    }
  },
  watch: {
    localSelectedVehicle(newVal, oldVal) {
      console.log('local ', newVal, oldVal)
      if (newVal == 'AUDI Q5') {
        this.vehicleStats.averageKm = 202180
        this.vehicleStats.vehicleType = 'OSOBNÍ AUTOMOBIL'
        this.vehicleStats.rank = 120
      } else if (newVal == 'ŠKODA OCTAVIA KOMBI') {
        this.vehicleStats.averageKm = 223981
        this.vehicleStats.vehicleType = 'OSOBNÍ AUTOMOBIL'
      } else if (newVal) {
        this.vehicleStats.rank = Math.floor(Math.random() * (10000 - 50) + 50);
        this.vehicleStats.averageKm = '---'
      } else {
        this.vehicleStats.averageKm = 158357
      }
      this.fillLineAgeData(newVal);
      this.fillLineKmData(newVal);
    }
  },
  methods: {
    fillLineAgeData(vehicle) {
      let data1, data2, data3;
      if (!vehicle) {
        data1 = [0.1, 0.33, 0.44, 0.45, 0.8, 1.2, 1.7, 2.8, 3.1, 3.8];
        data2 = [0, 0.12, 0.18, 0.55, 0.4, 0.33, 0.8, 1, 0.8, 1.4];
        data3 = [0, 0.04, 0.05, 0.07, 0.04, 0.05, 0.05, 0.07, 0.09, 0.13];
      } else if (this.selectedVehicle == 'AUDI Q5') {
        data1 = [0, 0.1, 0.05, 0.12, 0.6, 0.5, 1.1, 1.4, 1.8, 2.5];
        data2 = [0, 0.1, 0.1, 0.23, 0.25, 0.4, 0.5, 0.7, 0.7, 1.2];
        data3 = [0, 0, 0.04, 0.06, 0.01, 0.02, 0.02, 0.08, 0.07, 0.09];
      } else {
        data1 = [];
        data2 = [];
        data3 = [];
      }
      this.faultChartAgeDataCollection = {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        datasets: [
          {
            fill: false,
            label: 'Závady typu A',
            backgroundColor: '#79d6a6',
            borderColor: '#79d6a6',
            data: data1
          },
          {
            fill: false,
            label: 'Závady typu B',
            backgroundColor: '#52a5ff',
            borderColor: '#52a5ff',
            data: data2
          },
          {
            fill: false,
            label: 'Závady typu C',
            backgroundColor: '#e56a88',
            borderColor: '#e56a88',
            data: data3
          }
        ]
      }
    },
    fillLineKmData(vehicle) {
      let data1, data2, data3;
      if (!vehicle) {
        data1 = [0, 0.33, 0.44, 0.45, 0.8, 1.2, 1.7, 2.8, 3.1, 3.8];
        data2 = [0, 0.12, 0.18, 0.55, 0.4, 0.33, 0.8, 1, 0.8, 1.4];
        data3 = [0, 0.04, 0.05, 0.07, 0.04, 0.05, 0.05, 0.07, 0.09, 0.13];
      } else if (this.selectedVehicle == 'AUDI Q5') {
        data1 = [0, 0.22, 0.12, 0.2, 0.8, 0.9, 2, 3.2, 4, 4.1];
        data2 = [0, 0.1, 0.1, 0.23, 0.25, 0.4, 0.5, 0.7, 0.7, 1.2];
        data3 = [0, 0, 0.05, 0.07, 0.04, 0.03, 0.06, 0.08, 0.07, 0.2];
      } else {
        data1 = [];
        data2 = [];
        data3 = [];
      }
      this.faultChartKmDataCollection = {
        labels: [1, 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000],
        datasets: [
          {
            fill: false,
            label: 'Závady typu A',
            backgroundColor: '#79d6a6',
            borderColor: '#79d6a6',
            data: data1
          },
          {
            fill: false,
            label: 'Závady typu B',
            backgroundColor: '#52a5ff',
            borderColor: '#52a5ff',
            data: data2
          },
          {
            fill: false,
            label: 'Závady typu C',
            backgroundColor: '#e56a88',
            borderColor: '#e56a88',
            data: data3
          }
        ]
      }
    },
  }

}
</script>

<style scoped>
.rank-main {
  font-size: 16px;
  font-weight: 700;
}
.rank-2 {
  font-size: 15px;
  opacity: 0.8;
}
.rank-3 {
  font-size: 14px;
  opacity: 0.6;
}
.rank-4 {
  font-size: 13px;
  opacity: 0.5;

}
.rank-5 {
  font-size: 12px;
  opacity: 0.4;
}

</style>
