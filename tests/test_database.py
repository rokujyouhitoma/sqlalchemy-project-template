def test_import():
    from database import Base, engine
    assert Base
    assert engine

    # TODO
    print(Base)
    Base.metadata.create_all(engine)
