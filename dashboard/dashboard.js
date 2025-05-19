// Fetch the attack logs from the backend logs file (relative path may need adjustment when serving via HTTP)
fetch('../logs/attack_logs.json')
  .then(response => response.json())
  .then(data => {
    // Count occurrences of each attack phase
    const phaseCount = {};
    data.forEach(log => {
      const phase = log.phase || 'Unknown';
      phaseCount[phase] = (phaseCount[phase] || 0) + 1;
    });
    
    const labels = Object.keys(phaseCount);
    const counts = Object.values(phaseCount);
    
    // Render a bar chart with Chart.js
    const ctx = document.getElementById('attackChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Number of Events per Phase',
          data: counts,
          backgroundColor: 'rgba(255, 99, 132, 0.6)',
          borderColor: 'rgba(255, 99, 132, 1)',
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
  .catch(error => console.error('Error fetching attack logs:', error));
