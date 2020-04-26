<template>
    <div class="main-page">
      <b-container>
        <b-row>
          <b-col>
            <h2>Stanice technické kontroly</h2>
            <description :text="descriptionText"/>
          </b-col>
          <b-col>
            <filtration/>
          </b-col>
          <b-col>

          </b-col>
        </b-row>
        <b-row>
          <b-col cols="8">
            <cz-map :svgWidth="mapWidth" :svgHeight="mapHeight"/>
          </b-col>
          <b-col></b-col>
        </b-row>
        <b-row>

        </b-row>
      </b-container>




        <!-- <b-button size="sm" @click="toggle">
            {{ show ? 'Hide' : 'Show' }} Alert
        </b-button>
        <b-alert
            v-model="show"
            class="mt-3"
            dismissible
        >
            Hello {{ name }}!
        </b-alert> -->
    </div>
</template>

<script>
import Description from './Description'
import Filtration from './Filtration'
import CzMap from './CzMap'

export default {
  name: 'VisualizationIndex',
  components: {
    Description,
    Filtration,
    CzMap
  },
  data () {
    return {
      msg: 'Visualization Index page',
      show: true,
      name: "asdf",
      descriptionText: `
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit,
        vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus,
        ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique,
        tortor mauris molestie elit, et lacinia ipsum quam nec dui. Quisque nec
        mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit
      `,
      mapWidth: 900,
      mapHeight: 500,
    }
  },
  methods: {
    toggle() {
      this.show = !this.show
    }
  }
}
</script>
