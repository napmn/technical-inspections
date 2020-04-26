<template>
  <div>
    <b-row>
      <b-col>{{ title }}</b-col>
      <b-col cols="9">
        <b-form-select id="select" :options="options" v-model="selected"/>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'SelectItem',
  props: ['title', 'options'],
  data: function() {
    return {
      selected: null
    }
  }
}
</script>
