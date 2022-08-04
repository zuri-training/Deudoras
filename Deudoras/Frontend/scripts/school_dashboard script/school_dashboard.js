class School_dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = { sidebar: false };
  }
  render() {
    return (
      <div className="Container">
        <nav>
          <img
            src="../../assets/school_dashboard assets/project debtor logo svg 3 desktop.png"
            alt="logo"
          />
          <div>
            <img
              src="../../assets/school_dashboard assets/menu.png"
              alt="logo"
            />
            <div></div>
          </div>
        </nav>
      </div>
    );
  }
}
