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
        const response = await fetch('http://localhost:8000/api/get/body_weight/all_data');
        const data = await response.json();

        const numbers = data['data']['list'];
        let totalPercentageChange = 0;

        for (let i = 1; i < numbers.length; i++) {
            const currentValue = numbers[i];
            const previousValue = numbers[i - 1];

            const difference = currentValue - previousValue;
            const percentageChange = (difference / previousValue) * 100;

            totalPercentageChange += percentageChange;
        }

        let averagePercentageChange = totalPercentageChange / (numbers.length - 1);
        if (numbers.length === 1) {
            averagePercentageChange = 0;
        }

        return {
            "error": false,
            "list_weights": data['data']['list'],
            "average_weight": data['data']['average'],
            "evol_weight": averagePercentageChange
        }
    } catch (error) {
        console.log("ERROR OCCURRED: ", error);
        return {
            "error": true
        }
    }
}
