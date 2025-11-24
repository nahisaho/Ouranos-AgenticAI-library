export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-8">
          Ouranos Interactive Platform
        </h1>
        <p className="text-xl mb-4">
          Interactive AI Prompt Platform inspired by NotebookLM
        </p>
        <p className="mb-8">
          Browse 54+ specialized prompts across 11 professional domains.
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
          <a
            href="/prompts"
            className="p-6 border rounded-lg hover:bg-gray-100 transition"
          >
            <h2 className="text-2xl font-semibold mb-2">Prompts →</h2>
            <p>Browse our library of AI prompt templates</p>
          </a>
          
          <a
            href="/categories"
            className="p-6 border rounded-lg hover:bg-gray-100 transition"
          >
            <h2 className="text-2xl font-semibold mb-2">Categories →</h2>
            <p>Explore 11 professional domains</p>
          </a>
          
          <a
            href="/about"
            className="p-6 border rounded-lg hover:bg-gray-100 transition"
          >
            <h2 className="text-2xl font-semibold mb-2">About →</h2>
            <p>Learn more about Ouranos</p>
          </a>
        </div>
      </div>
    </main>
  )
}
