def agendar_consulta(paciente, medico):
    if not paciente or not medico:
        raise ValueError("Paciente e médico são obrigatórios")

    return f"Consulta agendada para {paciente} com Dr(a). {medico}"


if __name__ == "__main__":
    print(agendar_consulta("João Silva", "Ana Souza"))
