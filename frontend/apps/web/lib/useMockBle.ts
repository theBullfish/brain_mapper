import { useEffect } from 'react';
import BleBridge from './bleBridge';

export function useMockBle(userId:string){
  useEffect(()=>{
    const id=setInterval(()=>{
      const now=Date.now();
      BleBridge.postHRV({userId, ts:now, rr:800+Math.floor(Math.random()*40-20)});
      BleBridge.postBEN({userId, tsStart:now, ben: Math.random()*1.2});
    },4000);
    return ()=>clearInterval(id);
  },[userId]);
}
