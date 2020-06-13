<script>
import { Line, mixins } from 'vue-chartjs'


export default {
    name: 'LineChart',
    extends: Line,
    mixins: [mixins.reactiveProp], // creates prop called chartData and set watcher
    props: ['options'],
    mounted() {
        console.log('rendering line chart with data')
        console.log(this.chartData)
        this.renderChart(this.chartData, this.options)
    }
}
</script>
