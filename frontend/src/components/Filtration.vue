<template>
  <div class="filtration h-100 d-flex flex-column">
    <SearchItem :title="searchTitle" :text="searchText"/>
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
  props: ['selectedRegion'],
  data() {
    return {
      searchTitle: 'Vozidlo',
      searchText: 'Vyhledat vozidlo...',
      selectTitle: 'Kraj',
      selectOptions: [
        {value: null, text: 'Všechny kraje'},
        {value: 'Středočeský', text: 'Středočeský'},
        {value: 'Ústecký', text: 'Ústecký'},
        {value: 'Jihočeský', text: 'Jihočeský'},
        {value: 'Jihomoravský', text: 'Jihomoravský'},
        {value: 'Karlovarský', text: 'Karlovarský'},
        {value: 'Královéhradecký', text: 'Královéhradecký'},
        {value: 'Liberecký', text: 'Liberecký'},
        {value: 'Kraj Vysočina', text: 'Kraj Vysočina'},
        {value: 'Moravskoslezský', text: 'Moravskoslezský'},
        {value: 'Olomoucký', text: 'Olomoucký'},
        {value: 'Pardubický', text: 'Pardubický'},
        {value: 'Plzeňský', text: 'Plzeňský'},
        {value: 'Praha', text: 'Praha'},
        {value: 'Zlínský', text: 'Zlínský'}
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
    }
  },
}
</script>
