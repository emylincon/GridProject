var ctx = document.getElementById('resnet').getContext('2d');
var resnet = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ['Eczema', 'Healthy'],
        datasets: [{
            label: '% Predicted',
            data: [1,1],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },

            }],
            xAxes: [{
                gridLines: {
                    display: true,
                    color: 'rgb(211,211,211, 0.16)'
                  }
            }]
        },
        title: {
            text: "RESNET50 Base Model",
            display: true,
            fontStyle: 'bold',
        },
        legend: {
            display: false
         },
    }
});

var ctx1 = document.getElementById('eff').getContext('2d');
var eff = new Chart(ctx1, {
    type: 'horizontalBar',
    data: {
        labels: ['Eczema', 'Healthy'],
        datasets: [{
            label: '% Predicted',
            data: [1,1],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },

            }],
            xAxes: [{
                gridLines: {
                    display: true,
                    color: 'rgb(211,211,211, 0.16)'
                  }
            }]
        },
        title: {
            text: "InceptionV3 Base Model",
            display: true,
            fontStyle: 'bold',
        },
        legend: {
            display: false
         },
    }
});

var ctx2 = document.getElementById('incept').getContext('2d');
var incept = new Chart(ctx2, {
    type: 'horizontalBar',
    data: {
        labels: ['Eczema', 'Healthy'],
        datasets: [{
            label: '% Predicted',
            data: [1,1],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },

            }],
            xAxes: [{
                gridLines: {
                    display: true,
                    color: 'rgb(211,211,211, 0.16)'
                  }
            }]
        },
        title: {
            text: "EfficientNetB7 Base Model",
            display: true,
            fontStyle: 'bold',
        },
        legend: {
            display: false
         },
    }
});

function update_stat(){
    resnet.data.datasets[0].data = data.resnet;
    eff.data.datasets[0].data = data.efficient;
    incept.data.datasets[0].data = data.inception;

    resnet.update();
    eff.update();
    incept.update();
}

update_stat()
