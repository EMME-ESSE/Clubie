

const getDataColors = opacity => {
    const colors = ['rgba(255, 99, 132, 0.5)', 'rgba(54, 162, 235, 0.5)', 'rgba(255, 206, 86, 0.5)', 'rgba(75, 192, 192, 0.5)', 'rgba(153, 102, 255, 0.5)', 'rgba(255, 159, 64, 0.5)', 'rgba(136, 255, 156, 0.5)', 'rgba(235, 166, 54, 0.5)', 'rgba(132, 209, 235, 0.5)', 'rgba(255, 112, 197, 0.5)']
    return colors.map(color => opacity ? `${color + opacity}` : color)
}

const meses = (retiro, month) => {
    const mesesVentas = month.map(monthRange => {
        const [from, to] = monthRange.split('-')
        return coasters.filter(retiro => retiro.month >= from && retiro.month <= to).length
    })
    return mesesVentas
}

const updateChartData = (chartId, data, label) => {
    const chart = Chart.getChart(chartId)
    chart.data.datasets[0].data = data
    chart.data.datasets[0].label = label
    chart.update()
}