<template>
  <b-row class="h-100 d-flex align-items-center">
    <b-col class="ml-4"><h4>{{ title }}</h4></b-col>
    <b-col cols="7">
      <vue-simple-suggest v-model="localSelectedVehicle" :list="getSuggestionList" :filter-by-query="false"
          mode="select" :nullable-select="nullable">
        <input v-model="search" :placeholder="text">
      </vue-simple-suggest>
    </b-col>
    <b-col cols="2">
      <b-button variant="danger" @click="resetSearch">Reset</b-button>
    </b-col>
  </b-row>

</template>

<script>
export default {
  name: 'SearchItem',
  props: ['title', 'text', 'selectedVehicle'],
  data: function() {
    return {
      search: '',
      nullable: true
    }
  },
  computed: {
    localSelectedVehicle: {
      get: function() {
        return this.selectedVehicle;
      },
      set: function(value) {
        this.$emit('update:selectedVehicle', value);
      }
    }
  },
  methods: {
    getSuggestionList() {
      return this.axios.get('http://0.0.0.0:8000/vehicle-suggestions',
        {
          params: {
            'search': this.search
          }
        }
      ).then(response => response.data.map(c => c.name))
    },
    resetSearch() {
      this.localSelectedVehicle = '';
      this.search = '';
    }
  }
}
</script>
