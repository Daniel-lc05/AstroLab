from rocket.parts.part import Part


def build_vehicle():
    # Root body (reference frame origin)
    root = Part(
        name="Rocket",
        mass_dry=0.0,
        r_cg_local=[0, 0, 0],
        I_cg_local=[[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    )

    tank = Part(
        name="Tank",
        mass_dry=500,
        r_cg_local=[0, 0, 1.5],
        I_cg_local=[[100, 0, 0],
                    [0, 200, 0],
                    [0, 0, 100]],
        parent=root,
        p_parent_child=[0, 0, 0]
    )

    engine = Part(
        name="Engine",
        mass_dry=200,
        r_cg_local=[0, 0, 0.5],
        I_cg_local=[[50, 0, 0],
                    [0, 80, 0],
                    [0, 0, 50]],
        parent=root,
        p_parent_child=[0, 0, -1.0]
    )

    return RocketAssembly(root)


def main():
    rocket = build_vehicle()

    solver = RK4(dt=0.01)

    engine = SimulationEngine(
        vehicle=rocket,
        solver=solver,
        t0=0.0,
        tf=10.0
    )

    results = engine.run()

    results.save("outputs/run_001")

    print("Simulation finished.")


if __name__ == "__main__":
    main()