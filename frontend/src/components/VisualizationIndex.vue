<template>
    <div class="main-page">
      <b-container class="border rounded">
        <b-row>
          <b-col cols="8">
            <b-row class="pt-3">
              <b-col>
                <h2>Stanice technické kontroly</h2>
                <Description :text="descriptionText"/>
              </b-col>
              <b-col>
                <Filtration :selected-region.sync="selectedRegion" :selected-vehicle.sync="selectedVehicle"/>
              </b-col>
            </b-row>
            <b-row>
              <b-col>
                <CzMap :svgWidth="mapWidth" :svgHeight="mapHeight" :selected-region.sync="selectedRegion" :stations="stations"
                  :precalculated-stats="precalculatedStats"/>
              </b-col>
            </b-row>
          </b-col>
          <b-col cols="4" class="border-left mt-4 pl-5">
            <Vehicles :selected-vehicle.sync="selectedVehicle"/>
          </b-col>
        </b-row>
        <Stations :selected-region.sync="selectedRegion" :selected-vehicle.sync="selectedVehicle" :stations="stations"
          :precalculated-stats="precalculatedStats"/>
      </b-container>


    </div>
</template>

<script>
import Description from './Description'
import Filtration from './Filtration'
import CzMap from './CzMap'
import Stations from './Stations'
import Vehicles from './Vehicles'


export default {
  name: 'VisualizationIndex',
  components: {
    Description,
    Filtration,
    CzMap,
    Stations,
    Vehicles
  },
  data () {
    return {
      descriptionText: `
        Tento interaktivní dashboard zobrazuje statistiky technických kontrol z roku 2018.
        Použitá datová sada je volně dostupná na stránce <a href="https://data.gov.cz/">data.gov.cz</a>.
      `,
      mapWidth: 900,
      mapHeight: 500,
      selectedRegion: null,
      selectedVehicle: null,
      apiBaseUrl: 'http://localhost:8000',
      stations: null,
      precalculatedStats: null
    }
  },
  mounted() {
    this.axios.get(this.apiBaseUrl + '/stations').then((response) => {
      this.stations = response.data;
    });
    this.axios.get(this.apiBaseUrl + '/precalculated-stats').then((response) => {
      this.precalculatedStats = response.data;
    });
  }
}
</script>
