<script>
  import { onMount } from "svelte";
  import * as echarts from "echarts";

  let data = {};

  async function fetchData() {
    const response = await fetch("http://localhost:8000/data");
    data = await response.json();
    drawCharts();
  }

  function drawCharts() {
    let pieChart = echarts.init(document.getElementById("piechart"));
    let barChart = echarts.init(document.getElementById("barplot"));

    pieChart.setOption({
      title: { text: "Distribución de Productos" },
      series: [
        {
          type: "pie",
          data: data.piechart.labels.map((label, i) => ({
            name: label,
            value: data.piechart.values[i],
          })),
        },
      ],
    });

    barChart.setOption({
      title: { text: "Ventas Mensuales" },
      xAxis: { type: "category", data: data.barplot.categories },
      yAxis: { type: "value" },
      series: [{ type: "bar", data: data.barplot.values }],
    });
  }

  onMount(fetchData);
</script>

<div id="piechart" style="width: 600px; height: 400px;"></div>
<div id="barplot" style="width: 600px; height: 400px;"></div>
