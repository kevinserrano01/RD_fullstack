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

<div
  class="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4"
>
  <h1 class="text-2xl font-bold text-gray-800 mb-6">Visualización de Datos</h1>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-6xl">
    <div
      id="piechart"
      class="bg-white rounded-lg shadow-md p-4"
      style="width: 100%; height: 400px;"
    ></div>
    <div
      id="barplot"
      class="bg-white rounded-lg shadow-md p-4"
      style="width: 100%; height: 400px;"
    ></div>
  </div>
</div>
