<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body, .legend {
  background-color: #f1f4f6;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 20px;
}
.container {
  max-width: 1800px;
  background-color: #ffffff
}
/* CZ map */
.region {
  fill: #aaa;
}
/* .region {
  stroke: aqua;
} */
.region.unzoomed:hover {
  stroke-width:3px;
}

/* Tooplitp */
.d3-tip {
    line-height: 1.1rem;
    padding: 12px;
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    border-radius: 2px;
    pointer-events: none;
  }

.d3-tip-bold {
    font-weight: bold;
}

/* Creates a small triangle extender for the tooltip */
.d3-tip:after {
    box-sizing: border-box;
    display: inline;
    font-size: 10px;
    width: 100%;
    line-height: 1;
    color: rgba(0, 0, 0, 0.8);
    position: absolute;
    pointer-events: none;
}

/* Northward tooltips */
.d3-tip.n:after {
    content: "\25BC";
    margin: -1px 0 0 0;
    top: 100%;
    left: 0;
    text-align: center;
}

/* Eastward tooltips */
.d3-tip.e:after {
    content: "\25C0";
    margin: -4px 0 0 0;
    top: 50%;
    left: -8px;
}

/* Southward tooltips */
.d3-tip.s:after {
    content: "\25B2";
    margin: 0 0 1px 0;
    top: -8px;
    left: 0;
    text-align: center;
}

/* Westward tooltips */
.d3-tip.w:after {
    content: "\25B6";
    margin: -4px 0 0 -1px;
    top: 50%;
    left: 100%;
}

/* Stations */
#line-chart, #horizontalbar-chart {
  max-height: 200px;
  width: 100%;
}
</style>
