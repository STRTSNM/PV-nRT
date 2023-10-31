# shell.nix

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "python3.10-environment";

  buildInputs = [
    (pkgs.python310)
    (pkgs.python310Packages.numpy)
    (pkgs.python310Packages.noise)
    (pkgs.git)
    (pkgs.python310Packages.matplotlib)
    (pkgs.python310Packages.pygame)
    (pkgs.python310Packages.pygame-gui)
  ];
}
