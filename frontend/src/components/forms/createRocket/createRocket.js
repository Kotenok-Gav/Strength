// Создание графической ракеты

const Cube = () => {
    return (
        <div
            style={{
            width: '50px',
            height: '50px',
            backgroundColor: 'blue',
            margin: '10px',
            }}
        />
    );
};


const renderCubes = (start_rocket) => {
    const cubes = [];
    for (let i = 0; i < start_rocket; i++) {
        cubes.push(<Cube key={i} />);
    }
    return cubes;
};

export default renderCubes;