import { useEffect } from 'react';
import useMockBle from '../lib/useMockBle';
import useMockEeg from '../lib/useMockEeg';

export default function ControlEnergy() {
  useMockBle();
  useMockEeg();

  return <div><h1>🧪 Mock BLE/EEG Test</h1><p>Open the browser console to see connection logs.</p></div>;
}
