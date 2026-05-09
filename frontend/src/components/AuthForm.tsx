import { useState } from "react";
import { loginUser, registerUser } from "../services/api";

type AuthFormProps = {
  onLogin: () => void;
};

export function AuthForm({ onLogin }: AuthFormProps) {
  const [email, setEmail] = useState("victor@email.com");
  const [password, setPassword] = useState("123456");
  const [mode, setMode] = useState<"login" | "register">("login");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      if (mode === "register") {
        await registerUser(email, password);
        setMessage("Usuário cadastrado. Agora faça login.");
        setMode("login");
        return;
      }

      const data = await loginUser(email, password);
      localStorage.setItem("devflow_token", data.access_token);
      onLogin();
    } catch (error) {
      setMessage(error instanceof Error ? error.message : "Erro inesperado");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-950 text-white px-4">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-xl"
      >
        <h1 className="text-3xl font-bold mb-2">DevFlow AI</h1>
        <p className="text-slate-400 mb-6">
          {mode === "login"
            ? "Entre para acessar suas análises."
            : "Crie sua conta para começar."}
        </p>

        <label className="block text-sm mb-2">E-mail</label>
        <input
          className="w-full mb-4 p-3 rounded-lg bg-slate-800 border border-slate-700 outline-none"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
        />

        <label className="block text-sm mb-2">Senha</label>
        <input
          className="w-full mb-6 p-3 rounded-lg bg-slate-800 border border-slate-700 outline-none"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
        />

        {message && <p className="text-sm text-amber-400 mb-4">{message}</p>}

        <button
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 rounded-lg p-3 font-semibold disabled:opacity-60"
        >
          {loading ? "Processando..." : mode === "login" ? "Entrar" : "Cadastrar"}
        </button>

        <button
          type="button"
          className="w-full mt-4 text-sm text-slate-400 hover:text-white"
          onClick={() => setMode(mode === "login" ? "register" : "login")}
        >
          {mode === "login"
            ? "Ainda não tenho conta"
            : "Já tenho conta"}
        </button>
      </form>
    </div>
  );
}