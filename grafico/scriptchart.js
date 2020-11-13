var labels = [];
var ok_test = [];
var nok_test = [];
var ok_subtest = [];
var nok_subtest = [];
var data;

var config = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Ok tests',
            borderColor: window.chartColors.red,
            backgroundColor: window.chartColors.red,
            data: ok_test,
        }, {
            label: 'Not ok tests',
            borderColor: window.chartColors.blue,
            backgroundColor: window.chartColors.blue,
            data: nok_test,
        }, {
            label: 'Ok subtests ',
            borderColor: window.chartColors.green,
            backgroundColor: window.chartColors.green,
            data: ok_subtest,
        }, {
            label: 'Not ok subtests',
            borderColor: window.chartColors.yellow,
            backgroundColor: window.chartColors.yellow,
            data: nok_subtest,
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Test Anything Protocol'
        },
        tooltips: {
            mode: 'index',
        },
        hover: {
            mode: 'index'
        },
        scales: {
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Datas'
                }
            }],
            yAxes: [{
                stacked: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Quantidade total de testes'
                }
            }]
        }
    }
};

function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

window.onload = function () {
    readTextFile("data.json", function (text) {
        data = JSON.parse(text);
        console.log(data);

        try {
            data.items.map((item) => {
                labels.push(item.data);
                ok_test.push(item.ok_test);
                nok_test.push(item.nok_test);
                ok_subtest.push(item.ok_subtest);
                nok_subtest.push(item.nok_subtest);
            });
        } catch (error) {
            console.log(error);
        }
        var ctx = document.getElementById('canvas').getContext('2d');
        window.myLine = new Chart(ctx, config);
    });

};