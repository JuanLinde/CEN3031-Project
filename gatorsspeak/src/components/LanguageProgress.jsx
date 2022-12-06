import React from 'react'
import './LanguageProgress.css'
import { ProgressBar } from '.'
const LanguageProgress = (props) => {
    const flag = props.flag
    return (
        <div className='language-progress'>
            <p style={{
                margin: 'auto',
                textAlign: 'center'
            }}>{flag.content}</p>
            <div className='language-box'>
                <img className='lang-prog-img' src={flag.icon}></img>
                <ProgressBar done={70}/>
            </div>
        </div>
    )
}

export default LanguageProgress