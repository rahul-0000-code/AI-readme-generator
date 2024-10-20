import { Injectable, Cacheable } from '@nestjs/common';
import { Octokit } from '@octokit/rest';

@Injectable()
export class GithubService {
  private octokit: Octokit;

  constructor() {
    this.octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });
  }

  @Cacheable()
  async getRepoContent(owner: string, repo: string) {
    const { data } = await this.octokit.repos.getContent({
      owner,
      repo,
      path: '', // Root folder for now
    });
    return data;
  }
}
