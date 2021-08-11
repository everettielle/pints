#!/usr/bin/env python3
#
# Functional tests for HamiltonianMCMC
#
# This file is part of PINTS (https://github.com/pints-team/pints/) which is
# released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#
import pints
import pints.functionaltests as ft


def two_dim_gaussian(n_iterations=1000):
    """
    Tests :class:`pints.HamiltonianMCMC`
    on a two-dimensional Gaussian distribution with true solution
    ``[0, 0]`` and returns a dictionary with entries ``kld`` and ``mean-ess``.

    For details of the solved problem, see
    :class:`pints.functionaltests.RunMcmcMethodOnTwoDimGaussian`.
    """
    n_warmup = 200
    if n_warmup > n_iterations // 2:
        n_warmup = n_iterations // 10

    problem = ft.RunMcmcMethodOnTwoDimGaussian(
        method=pints.HamiltonianMCMC,
        n_chains=4,
        n_iterations=n_iterations,
        n_warmup=n_warmup,
        method_hyper_parameters=[20, 1]
    )

    return {
        'kld': problem.estimate_kld(),
        'mean-ess': problem.estimate_mean_ess()
    }


def banana(n_iterations=2000):
    """
    Tests :class:`pints.HamiltonianMCMC`
    on a two-dimensional "twisted Gaussian" distribution with true solution
    ``[0, 0]`` and returns a dictionary with entries ``kld`` and ``mean-ess``.

    For details of the solved problem, see
    :class:`pints.functionaltests.RunMcmcMethodOnBanana`.
    """
    n_warmup = 1000
    if n_warmup > n_iterations // 2:
        n_warmup = n_iterations // 10

    problem = ft.RunMcmcMethodOnBanana(
        method=pints.HamiltonianMCMC,
        n_chains=4,
        n_iterations=n_iterations,
        n_warmup=n_warmup,
        method_hyper_parameters=[20, 2]
    )

    return {
        'kld': problem.estimate_kld(),
        'mean-ess': problem.estimate_mean_ess()
    }


def high_dim_gaussian(n_iterations=4000):
    """
     Tests :class:`pints.HamiltonianMCMC`
    on a 20-dimensional Gaussian distribution centered at the origin, and
    returns a dictionary with entries ``kld`` and ``mean-ess``.

    For details of the solved problem, see
    :class:`pints.functionaltests.RunMcmcMethodOnHighDimensionalGaussian`.
    """
    n_warmup = 1000
    if n_warmup > n_iterations // 2:
        n_warmup = n_iterations // 10

    problem = ft.RunMcmcMethodOnHighDimensionalGaussian(
        method=pints.HamiltonianMCMC,
        n_chains=4,
        n_iterations=n_iterations,
        n_warmup=n_warmup,
        method_hyper_parameters=[20, 1]
    )

    return {
        'kld': problem.estimate_kld(),
        'mean-ess': problem.estimate_mean_ess()
    }
