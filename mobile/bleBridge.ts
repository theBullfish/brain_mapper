import { Capacitor, registerPlugin } from '@capacitor/core';

export interface BleBridgePlugin {
  postHRV(options:{userId:string, ts:number, rr:number}):Promise<void>;
  postBEN(options:{userId:string, tsStart:number, ben:number}):Promise<void>;
}

const BleBridge = Capacitor.isNativePlatform()
  ? registerPlugin<BleBridgePlugin>('BleBridge')
  : {
      async postHRV(o:any){ await fetch('/api/ble/hrv',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(o)}); },
      async postBEN(o:any){ await fetch('/api/ble/ben',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(o)}); },
    };

export default BleBridge;
