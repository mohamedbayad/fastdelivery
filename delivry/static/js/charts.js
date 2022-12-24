// // charts js
// const ctx = document.getElementById('myChart').getContext('2d');
// const myDash = document.getElementById('mydash').getContext('2d');
// const myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
//         datasets: [{
//             label: "colis",
//             data: [12, 19, 3, 5, 2, 3, 20],
//             backgroundColor: [
//                 'rgba(239, 206, 250)',
//                 'rgba(212, 178, 216)',
//                 'rgba(168, 143, 172)',
//                 'rgba(130, 108, 127)',
//                 'rgba(93, 78, 96)',
//                 'rgba(208, 209, 255)',
//                 'rgba(216, 187, 255)',
//             ],
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         },
//         responsive : true
//     }
// });

// const myChartTwo = new Chart(myDash, {
//     type: 'line',
//     data: {
//         labels: [],
//         datasets: [{
//             label: "colis",
//             data: [],
//             backgroundColor: [
//                 'rgba(239, 206, 250)',
//                 'rgba(212, 178, 216)',
//                 'rgba(168, 143, 172)',
//                 'rgba(130, 108, 127)',
//                 'rgba(93, 78, 96)',
//                 'rgba(208, 209, 255)',
//             ],
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         },
//         responsive : true
//     },
// });

// for (let c of listCity) {
//     myChartTwo.data.labels.push(c.city)
//     myChartTwo.data.datasets[0].data.push(c.number)
//     console.log(c)
// }


