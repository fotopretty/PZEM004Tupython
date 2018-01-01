# PZEM004Tupython
ESP8266 ESP32 ESP32s  communication library for Peacefair PZEM-004T Energy monitor

Serial communication
This module is equipped with TTL serial data communication interface, you can read and set the relevant parameters via the serial port; but if you want to communicate with a device which has USB or RS232 (such as computer), you need to be equipped with different TTL pin board (USB communication needs to be equipped with TTL to USB pin board; RS232 communication needs to be equipped with TTL to RS232 pin board), the specific connection type as shown in Figure 2. In the below table are the communication protocols of this module:

<table>
<thead>
<tr>
<th>No</th>
<th align="center">Function</th>
<th align="center">Head</th>
<th>Data1- Data5</th>
<th align="center">Sum</th>
</tr>
</thead>
<tbody>
<tr>
<td>1a</td>
<td align="center">Voltage Req</td>
<td align="center">B0</td>
<td>C0 A8 01 01 00 (Computer sends a request to read the voltage value)</td>
<td align="center">1A</td>
</tr>
<tr>
<td>1b</td>
<td align="center">Voltage Resp</td>
<td align="center">A0</td>
<td>00 E6 02 00 00 (Meter reply the voltage value is 230.2V)</td>
<td align="center">88</td>
</tr>
<tr>
<td>2a</td>
<td align="center">Current Req</td>
<td align="center">B1</td>
<td>C0 A8 01 01 00 (Computer sends a request to read the current value)</td>
<td align="center">1B</td>
</tr>
<tr>
<td>2b</td>
<td align="center">Current Resp</td>
<td align="center">A1</td>
<td>00 11 20 00 00 (Meter reply the current value is 17.32A)</td>
<td align="center">D2</td>
</tr>
<tr>
<td>3a</td>
<td align="center">Active power Req</td>
<td align="center">B2</td>
<td>C0 A8 01 01 00 (Computer sends a request to read the active power value)</td>
<td align="center">1C</td>
</tr>
<tr>
<td>3b</td>
<td align="center">Active power Resp</td>
<td align="center">A2</td>
<td>08 98 00 00 00 (Meter reply the active power value is 2200w)</td>
<td align="center">42</td>
</tr>
<tr>
<td>4a</td>
<td align="center">Read energy Req</td>
<td align="center">B3</td>
<td>C0 A8 01 01 00 (Computer sends a request to read the energy value)</td>
<td align="center">1D</td>
</tr>
<tr>
<td>4b</td>
<td align="center">Read energy Resp</td>
<td align="center">A3</td>
<td>01 86 9f 00 00 (Meter reply the energy value is 99999wh)</td>
<td align="center">C9</td>
</tr>
<tr>
<td>5a</td>
<td align="center">Set the module address Req</td>
<td align="center">B4</td>
<td>C0 A8 01 01 00 (Computer sends a request to set the address, the address is 192.168.1.1)</td>
<td align="center">1E</td>
</tr>
<tr>
<td>5b</td>
<td align="center">Set the module address resp</td>
<td align="center">A4</td>
<td>00 00 00 00 00 (Meter reply the address was successfully set)</td>
<td align="center">A4</td>
</tr>
<tr>
<td>6a</td>
<td align="center">Set the power alarm threshold Req</td>
<td align="center">B5</td>
<td>C0 A8 01 01 14 (computer sends a request to set a power alarm threshold)</td>
<td align="center">33</td>
</tr>
<tr>
<td>6b</td>
<td align="center">Set the power alarm threshold Resp</td>
<td align="center">A5</td>
<td>00 00 00 00 00 (Meter reply the power alarm threshold  was successfully set)</td>
<td align="center">A5</td>
</tr></tbody></table>
