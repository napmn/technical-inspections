<template>
  <div>
    <b-row>
      <b-col>{{ title }}</b-col>
      <b-col cols="9">
        <b-form-input v-model="search" :placeholder="text"/>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'SearchItem',
  props: ['title', 'text'],
  data: function() {
    return {
      search: null
    }
  }
}
</script>
