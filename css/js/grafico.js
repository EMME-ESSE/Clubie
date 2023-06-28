fetch('/prueba')
  .then(response => response.json())
  .then(data => {
    // Preparar los datos para el gráfico
    const labels = data.map(user => user.name);
    const values = data.map(user => user.telefono);

    // Configurar y generar el gráfico utilizando Chart.js
    const ctx = document.getElementById('modelsChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Teléfonos',
          data: values,
          backgroundColor: 'rgba(0, 123, 255, 0.5)',
          borderColor: 'rgba(0, 123, 255, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });