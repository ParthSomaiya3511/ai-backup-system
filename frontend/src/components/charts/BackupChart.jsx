import {

  LineChart,
  Line,
  XAxis,
  YAxis

} from "recharts";

const data = [

  { day: "Mon", backups: 20 },

  { day: "Tue", backups: 35 },

  { day: "Wed", backups: 50 },

  { day: "Thu", backups: 40 },

  { day: "Fri", backups: 70 }

];

export default function BackupChart() {

  return (

    <LineChart
      width={500}
      height={300}
      data={data}
    >

      <XAxis dataKey="day" />

      <YAxis />

      <Line
        type="monotone"
        dataKey="backups"
      />

    </LineChart>

  );

}