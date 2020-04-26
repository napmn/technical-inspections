<template>
  <div class="filtration">
    <SearchItem :title="searchTitle" :text="searchText"/>
    <SelectItem :title="selectTitle" :options="selectOptions"/>
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
  data() {
    return {
      searchTitle: 'Vozidlo',
      searchText: 'Vyhledat vozidlo...',
      selectTitle: 'Kraj',
      selectOptions: [
        {value: null, text: 'Všechny kraje'},
        {value: 'a', text: 'Nejaky kraj'},
        {value: 'b', text: 'Nejaky iny kraj'}
      ]
    }
  }
}
</script>
