async function fetchData() {
    try {
        console.log("Fetching data from API...");
        const response = await fetch('http://localhost:5000/api/data');
        console.log("Response status:", response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Fetched Data:", data); // Log data for debugging
        
        // Ensure data was retrieved and is not empty
        if (data.length === 0) {
            console.warn("Warning: Fetched data is empty.");
        }

        // Pass data to update the UI
        updateDashboard(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}


function updateDashboard(data) {
    // Update Summary
    const totalDomestic = data.reduce((sum, item) => sum + item.domestic_2019_20, 0);
    const totalForeign = data.reduce((sum, item) => sum + item.foreign_2019_20, 0);

    document.getElementById('total-domestic').textContent = totalDomestic;
    document.getElementById('total-foreign').textContent = totalForeign;
    document.getElementById('total-monuments').textContent = data.length;

    // Populate Table
    const tableBody = document.getElementById('data-table');
    tableBody.innerHTML = ''; // Clear existing rows
    data.forEach(item => {
        const row = `<tr>
            <td>${item.circle}</td>
            <td>${item.monument_name}</td>
            <td>${item.domestic_2019_20}</td>
            <td>${item.foreign_2019_20}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });

    // Create Chart
    createChart(data);
}


// Create a Chart
function createChart(data) {
    const ctx = document.getElementById('visitorChart').getContext('2d');
    const labels = data.map(item => item.monument_name);
    const domesticData = data.map(item => item.domestic_2019_20);
    const foreignData = data.map(item => item.foreign_2019_20);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Domestic Visitors',
                    data: domesticData,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                },
                {
                    label: 'Foreign Visitors',
                    data: foreignData,
                    backgroundColor: 'rgba(255, 99, 132, 0.6)',
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'Monuments' } },
                y: { title: { display: true, text: 'Visitors' } }
            }
        }
    });
}

// Fetch data on page load
fetchData();
