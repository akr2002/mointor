{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, self, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
      buildInputs = with pkgs; [
        (python3.withPackages(ps: with ps; [
          ipython
          requests
        ]))
      ];
      monitor = pkgs.stdenv.mkDerivation {
        name = "monitor";
        propagatedBuildInputs = buildInputs;
        dontUnpack = true;
        installPhase = "install -Dm755 ${./monitor.py} $out/bin/monitor";
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = buildInputs;
        shellHook = "";
      };
      packages.default = monitor;
    }
  );
}
