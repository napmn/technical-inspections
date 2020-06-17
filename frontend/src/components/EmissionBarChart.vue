<script>
import { Bar, mixins } from 'vue-chartjs'


export default {
    name: 'EmissionBarChart',
    extends: Bar,
    mixins: [mixins.reactiveProp], // creates prop called chartData and set watcher
    props: ['options'],
    mounted() {
        console.log('rendering emission Bar chart data')
        console.log(this.chartData)
        this.renderChart(this.chartData, this.options)
    }
}
</script>
