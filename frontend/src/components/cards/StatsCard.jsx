export default function StatsCard({
  title,
  value
}) {

  return (

    <div className="bg-slate-800 p-6 rounded-xl">

      <h3 className="text-gray-400">

        {title}

      </h3>

      <h1 className="text-3xl font-bold">

        {value}

      </h1>

    </div>

  );

}