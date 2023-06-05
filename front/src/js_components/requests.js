export function fetchData() {
    fetch('http://localhost:8000/api/data')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log("ERROR OCCURED: ", error)
        });
}

export async function fetchWeights() {
    try {
        const response = await fetch('http://localhost:8000/api/data/weights');
        const data = await response.json();

        const numbers = data['weights'];
        const sum = numbers.reduce((acc, curr) => acc + curr, 0);
        let totalPercentageChange = 0;

        for (let i = 1; i < numbers.length; i++) {
            const currentValue = numbers[i];
            const previousValue = numbers[i - 1];

            const difference = currentValue - previousValue;
            const percentageChange = (difference / previousValue) * 100;

            totalPercentageChange += percentageChange;
        }

        const averagePercentageChange = totalPercentageChange / (numbers.length - 1);

        return {
            "error": false,
            "list_weights": data['weights'],
            "mean_weight": sum / numbers.length,
            "evol_weight": averagePercentageChange
        }
    } catch (error) {
        console.log("ERROR OCCURRED: ", error);
        return {
            "error": true
        }
    }
}
