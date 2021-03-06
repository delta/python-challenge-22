defmodule PythonChallenge.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    unless Mix.env == :prod do
      Dotenv.load
      Mix.Task.run("loadconfig")
    end

    children = [
      # Start the Ecto repository
      PythonChallenge.Repo,
      # Start the Telemetry supervisor
      PythonChallengeWeb.Telemetry,
      # Start the PubSub system
      {Phoenix.PubSub, name: PythonChallenge.PubSub},
      # Start the Endpoint (http/https)
      PythonChallengeWeb.Endpoint
      # Start a worker by calling: PythonChallenge.Worker.start_link(arg)
      # {PythonChallenge.Worker, arg}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: PythonChallenge.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    PythonChallengeWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
