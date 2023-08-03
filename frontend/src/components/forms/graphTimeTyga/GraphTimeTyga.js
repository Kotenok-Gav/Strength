import React from 'react';
import { Line } from 'react-chartjs-2';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const Graph = ({ dataX, dataY }) => {
    const data = {
        labels: dataX,
        datasets: [
            {
                label: 'Примерный набор данных',
                data: dataY,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.3,
            },
        ],
    };

    return (
        <div>
            <Line data={data} />
        </div>
    );
};

export default Graph;
