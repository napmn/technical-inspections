<template>
  <div class="filtration h-100 d-flex flex-column">
    <SearchItem :title="searchTitle" :text="searchText" :selected-vehicle.sync="localSelectedVehicle"/>
    <SelectItem :title="selectTitle" :options="selectOptions" :selected-item.sync="localSelectedRegion"/>
  </div>
</template>

<script>
import SearchItem from './SearchItem'
import SelectItem from './SelectItem'

export default {
  name: 'Filtration',
  components: {
    SearchItem,
    SelectItem
  },
  props: ['selectedRegion', 'selectedVehicle'],
  data() {
    return {
      searchTitle: 'Vozidlo',
      searchText: 'Vyhledat vozidlo...',
      selectTitle: 'Kraj',
      selectOptions: [
        {value: null, text: 'Všechny kraje'},
        {value: 'Středočeský kraj', text: 'Středočeský'},
        {value: 'Ústecký kraj', text: 'Ústecký'},
        {value: 'Jihočeský kraj', text: 'Jihočeský'},
        {value: 'Jihomoravský kraj', text: 'Jihomoravský'},
        {value: 'Karlovarský kraj', text: 'Karlovarský'},
        {value: 'Královéhradecký kraj', text: 'Královéhradecký'},
        {value: 'Liberecký kraj', text: 'Liberecký'},
        {value: 'Vysočina', text: 'Vysočina'},
        {value: 'Moravskoslezský kraj', text: 'Moravskoslezský'},
        {value: 'Olomoucký kraj', text: 'Olomoucký'},
        {value: 'Pardubický kraj', text: 'Pardubický'},
        {value: 'Plzeňský kraj', text: 'Plzeňský'},
        {value: 'Hlavní město Praha', text: 'Hlavní město Praha'},
        {value: 'Zlínský kraj', text: 'Zlínský'}
      ]
    }
  },
  computed: {
    // to propagate change of selected region to parent component
    localSelectedRegion: {
      get: function() {
        return this.selectedRegion;
      },
      set: function(value) {
        console.log('REGION CHANGED IN FILTRATION ' + value);
        this.$emit('update:selectedRegion', value);
      }
    },
    localSelectedVehicle: {
      get: function() {
        return this.selectedVehicle;
      },
      set: function(value) {
        console.log('VEHICLE WAS SEARCHED AND SELECTED ' + value);
        this.$emit('update:selectedVehicle', value);
      }
    }
  },
}
</script>
