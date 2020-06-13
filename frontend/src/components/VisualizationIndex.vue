<template>
    <div class="main-page">
      <b-container>
        <b-row class="border">
          <b-col cols="8">
            <b-row>
              <b-col class="border">
                <h2>Stanice technické kontroly</h2>
                <Description :text="descriptionText"/>
              </b-col>
              <b-col class="border">
                <Filtration :selected-region.sync="selectedRegion"/>
              </b-col>
            </b-row>
            <b-row>
              <b-col class="border">
                <CzMap :svgWidth="mapWidth" :svgHeight="mapHeight" :selected-region.sync="selectedRegion"/>
              </b-col>
            </b-row>
          </b-col>
          <b-col cols="4">
            <Vehicles/>
          </b-col>
        </b-row>
        <Stations :selected-region="selectedRegion"/>
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
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit,
        vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus,
        ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique,
        tortor mauris molestie elit, et lacinia ipsum quam nec dui. Quisque nec
        mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit
      `,
      mapWidth: 900,
      mapHeight: 500,
      selectedRegion: null
    }
  },
}
</script>
