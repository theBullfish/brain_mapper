import { useState, useRef } from 'react'

export default function ControlEnergyTask() {
  const startRef = useRef(Date.now())
  const [val,setVal] = useState(50)
  const [done,setDone] = useState(false)

  async function submit(){
    const latency = Date.now()-startRef.current
    await fetch('/api/answers',{method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({user_id:'parent', ts:Date.now(), value:val, latency_ms:latency})
    })
    setDone(true)
  }

  if(done) return <p className='p-4 text-green-400'>Recorded ✔</p>

  return(
    <div className='flex flex-col items-center text-white p-6'>
      <h1 className='mb-4 text-xl'>Task‑switch effort (0–100)</h1>
      <input type='range' min={0} max={100} value={val} onChange={e=>setVal(Number(e.target.value))} className='w-full'/>
      <span className='text-2xl my-2'>{val}</span>
      <button onClick={submit} className='bg-blue-600 px-4 py-2 rounded'>Submit</button>
    </div>
  )
}
