import PropTypes from 'prop-types'

function Students(props) {
    return (
        <div className="student">
            <p>Name: {props.name}</p>
            <p>Age: {props.age}</p>
            <p>Student: {props.isStudent ? "YES" : "No"}</p>
        </div>
    );

}
Students.propTypes = {
    name: PropTypes.string,
    age: PropTypes.number,
    isStudent: PropTypes.bool,
}

Students.defaultProps = {
    name: "Guest",
    age: 0,
    isStudent: false,
}

export default Students;