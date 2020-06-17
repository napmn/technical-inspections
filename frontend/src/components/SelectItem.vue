<template>
  <b-row class="h-100 d-flex align-items-center">
    <b-col class="ml-4"><h4>{{ title }}</h4></b-col>
    <b-col cols="9">
      <b-form-select id="select" :options="options" v-model="localSelectedItem"/>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: 'SelectItem',
  props: ['title', 'options', 'selectedItem'],
  computed: {
    localSelectedItem: {
      get: function() {
        return this.selectedItem;
      },
      set: function(value) {
        this.$emit('update:selectedItem', value);
      }
    }
  },
}
</script>
