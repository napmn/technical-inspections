<script>
import { HorizontalBar, mixins } from 'vue-chartjs'


export default {
    name: 'BarChart',
    extends: HorizontalBar,
    mixins: [mixins.reactiveProp], // creates prop called chartData and set watcher
    props: ['options'],
    mounted() {
        console.log('rendering Bar chart data')
        console.log(this.chartData)
        this.renderChart(this.chartData, this.options)
    }
}
</script>
