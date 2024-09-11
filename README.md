# Monitor
Report website's status

## Usage
### Oneshot
```nix
nix run github:akr2002/monitor
```
### Persistent
Add the following line to your `flake.nix`
```nix
inputs.monitor.url = "github/akr2002:monitor";
```
Add the following to your `home.nix`
```nix
systemd.user.timers.monitor = {
    Install.WantedBy = [ "timers.target" ];
    Timer = {
        OnBootSec = "1m";
        OnUnitActiveSec = "1m";
        Unit = "monitor.service";
    };
};
systemd.user.services.monitor = {
    Unit = {
        Description = "A script to monitor websites.";
    };
    Install = {
        WantedBy = [ "default.target" ];
    };
    Service = {
        ExecStart = "${inputs.monitor.packages.${pkgs.system}.default}/bin/monitor";
    };
};
```
Start:
```bash
systemctl --user start mointor.timer
```
