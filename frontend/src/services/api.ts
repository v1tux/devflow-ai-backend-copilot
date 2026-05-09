const API_URL = "http://127.0.0.1:8000";

export async function registerUser(email: string, password: string) {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    throw new Error("Erro ao cadastrar usuário");
  }

  return response.json();
}

export async function loginUser(email: string, password: string) {
  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const response = await fetch(`${API_URL}/auth/token`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Credenciais inválidas");
  }

  return response.json();
}

export async function getAnalyses() {
  const token = localStorage.getItem("devflow_token");

  const response = await fetch(`${API_URL}/analyses`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error("Erro ao buscar análises");
  }

  return response.json();
}