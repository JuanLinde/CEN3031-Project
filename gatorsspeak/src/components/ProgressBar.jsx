import React from 'react'
import './ProgressBar.css'
const ProgressBar = ({done}) => {
    const [style, setStyle] = React.useState({done})

    // setStyle(
    //     {
    //         opacity: 1,
    //         width: `${done}%`
    //     }
    // )
    return (
        <div className='progress'>
            <div className='progress-done' style={{
                            opacity: 1,
                            width: `${done}%`
                        }}>
                <p>{done}%</p>
            </div>
        </div>
    )
}

export default ProgressBar